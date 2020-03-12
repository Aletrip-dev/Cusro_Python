import sqlite3

class Endereco(object):
    def __init__(self):
        self.cep = None
        self.logradouro = None
        self.complemento = None
        self.bairro = None
        self.localidade = None
        self.uf = None
        self.unidade = None
        self.ibge = None
        self.gia = None

    def criar_tabela(self): #cria metodo para criar tabela
        conn = sqlite3.connect("Enderecos.db")
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Endereco
        (cep text, logradouro text, complemento text, bairro text, Localidade text, uf text, 
        unidade text, ibge text, gia text)""")
        conn.commit()

    def salvar(self): 
        self.criar_tabela()
        conn = sqlite3.connect("Enderecos.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Endereco VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(self.cep, self.logradouro,
        self.complemento,self.bairro,self.localidade,self.uf,self.unidade,self.ibge,self.gia))
        conn.commit()
        print('CEP: %s encontrado e salvo com sucesso !!!'%self.cep)
