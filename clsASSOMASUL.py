import pyodbc
import time

from selenium import webdriver
from ConexaoSQL import ConexaoSQL
from datetime import datetime

class clsASSOMASUL(object):
    """description of class"""

    def __init__(self, url="http://diariooficialms.com.br/assomasul?pagina=filtro-avancado", strMunicipio="TRÊS LAGOAS", strDtIni="", strDtFim="", strDwnldPath="C:\\Users\\All Users\\tmpDownloads\\ASSOMASUL\\"):
        self.url = url
        self.strMunicipio = strMunicipio
        self.strDtIni = strDtIni
        self.strDtFim = strDtFim
        self.strDwnldPath = strDwnldPath
        #####return super().__init__(self, strMunicipio, strDtIni, strDwnldPath)
        pass

    def GetAllData(self):
        chOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory" : self.strDwnldPath}
        chOptions.add_experimental_option("prefs", prefs);

        path = self.strDwnldPath
        
        #"C:\\Users\\All Users\\tmpDownloads\\ASSOMASUL\\"
        #gPath = "C:\\Windows\\System32\\geckodriver.exe"
        #ffoxPath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    
        self.url = "http://diariooficialms.com.br/assomasul?pagina=filtro-avancado"

        driver = webdriver.Chrome(chrome_options=chOptions, executable_path="C:\\Program Files (x86)\\Google\\Drive\\chromedriver.exe")
        driver.get(self.url)

        time.sleep(6)
        
        #Busca o campo MUNICIPIO e efetua um click selecionando o municipio de TRÊS LAGOAS
        driver.find_element_by_xpath("//select[@name='filtro[municipio_id]']/option[text()='" + self.strMunicipio + "']").click()

        #Busca o campo da DATA_INICIAL e depois atribui uma data inicial de pesquisa
        elDataIni = driver.find_element_by_xpath("//input[@name='filtro[data_inicial]']")
        elDataIni.send_keys(self.strDtIni)

        #Busca o campo da DATA_FINAL e depois atribui uma data final de pesquisa
        elDataFim = driver.find_element_by_xpath("//input[@name='filtro[data_final]']")
        elDataFim.send_keys(self.strDtFim)

        #Busca o botao de pesquisar e efetua o CLICK
        strPathButton = r"//button[@class='btn btn-primary']"   
        submit_button = driver.find_element_by_xpath(strPathButton)
        submit_button.click()

        #Fica em idle por 10s para dar tempo de carregar a pagina
        time.sleep(10)

        linhas = driver.find_elements_by_tag_name("tr")
        ###(r"//tr[@role='row']")

        #CONNECTION    
        cn = ConexaoSQL("JK-DELL-2016\JK_SQL_SERVER","dbSCRAPING")

        cn = cn.ConnectarSQL()

        COMMANDO = ""

        i=0
        for linha in linhas:  
           i=i+1

           if i>1 and linha.text:
        
               #print(i)
               #print(linha.text)

               colunas = linha.find_elements_by_tag_name("td")
               if len(colunas) > 1:
                   #print(colunas[0].text)  ### TITULO
                   #print(colunas[1].text)  ### DATA
                   #print(colunas[2].text)  ### BOTAO BAIXAR
                   formulario = colunas[2].find_element_by_tag_name("form")
                   #print(formulario.get_attribute("action"))
                   strPathPDF = formulario.get_attribute("action")
                   #break
           
                   botao = formulario.find_element_by_tag_name("button")
                   botao.click()
           
                   time.sleep(10)
            
                   COMMANDO = ""

                   COMMANDO = "INSERT INTO tbDIARIO_OFICIAL(dt_publicacao, desc_publicacao, nome_arquivo, conteudo_publicacao) VALUES(?,?,?,?) "

                   curLocal = cn.execute(COMMANDO, (datetime.strptime(str(colunas[1].text),'%d/%m/%Y'), str(colunas[0].text), str(CorrigeNome(colunas[0].text)), str("") ))
                   cn.commit()
                   try:
                       teste = curLocal.insert_id()
                       teste1 = curLocal.lastrowid
                   except: 
                       print("Erro ao retornar o ID do Insert")
                   finally:
               
                       cn.rollback()
                       COMMANDO = ""

                   #print("Nome Corrigido:")
                   #print(CorrigeNome(colunas[0].text))
           pass
        cn.close()


    
        ##Acessa o site e obtem o objeto da pagina url
        dirs = os.listdir(strDwnldPath)
        # This prints all the files and directories (in our case it will be one file)
        #CONNECTION    
        cn = ConexaoSQL("JK-DELL-2016\JK_SQL_SERVER","dbDIARIO_OFICIAL")
        cn = cn.ConnectarSQL()


        for file in dirs:
           #print (file)

           with fitz.open(path + file) as doc:
            safe_text = ""
            for page in doc:
                safe_text += page.getText()
                #print(safe_text)
                COMMANDO = ( 
                                "UPDATE tbDIARIO_OFICIAL SET conteudo_publicacao = '" + str(safe_text) + 
                                "' WHERE nome_arquivo = '" + str(file).replace(".pdf","") + "' " +
                                " AND (conteudo_publicacao = '' OR conteudo_publicacao IS NULL)"
                           )
                #COMMANDO = COMMANDO.replace('-n0-', '-no-')
                ret = cn.execute(COMMANDO)
                cn.commit()
                if ret.rowcount == 0 :
                   COMMANDO = COMMANDO.replace('-no-', '-n0-')
                   ret = cn.execute(COMMANDO)
                   cn.commit()
                #print(COMMANDO)
                pass ### for page in doc
            pass ### with fitz
        pass ### GetAllData()
