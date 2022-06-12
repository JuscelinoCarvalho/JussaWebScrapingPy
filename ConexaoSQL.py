import pyodbc

class ConexaoSQL():
    """Classe para efetuar a conexão com o banco de dados MS SQL Server. Criado por Juselino Alves de Carvalho em 12-Abr-2020 13:51h."""
    
    def __init__(self, srvName, dbName):
            self.srvName = srvName
            self.dbName = dbName

    def ConnectarSQL(self):
        #srvName = "JK-DELL-2016\JK_SQL_SERVER" 
        #dbName = "Tributacao"
        string_conexao = "Driver={SQL Server}; Server=" + self.srvName + "; Database=" + self.dbName + "; Trusted_Connection=yes;"
        conexao = pyodbc.connect(string_conexao)
        return conexao

