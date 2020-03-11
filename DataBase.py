import sqlite3

conn = sqlite3.connect("teste.db") #cria tabela com o nome passado
cursor = conn.cursor()


def criar_tabela(): #cria metodo para criar tabela
    sql = """CREATE TABLE ALBUMS (Titulo text, Artista text, Data_lancamento text, Data_Publ text, Midia text)"""
    cursor.execute(sql)
    conn.commit()

def gravar_dados(): #cria método para gravar dados
    sql = """INSERT INTO ALBUMS VALUES ('Alex', 'Linking Park', '14/05/1999', '28/09/2000', 'MP3')"""
    cursor.execute(sql)
    conn.commit()

def gravar_muitos(): #método que grava diversos registros no banco
    ALBUMS = [('Lucas','Metálica','12/02/2020','14/02/2015', 'DVD'),
    ('Gabriel','Ironmanden','24/02/1982','12/03/2020','CD')]
    cursor.executemany("INSERT INTO ALBUMS VALUES(?,?,?,?,?)",ALBUMS)
    conn.commit()

def atualiza(): #faz UPDATE na tabela e altera o nome
    sql = """UPDATE ALBUMS SET Titulo = 'Alexandro'
    WHERE Titulo = 'Alex'
    """
    cursor.execute(sql)
    conn.commit()

def excluir(): #Deleta o registro onde o nome aparece
    sql = """DELETE FROM ALBUMS WHERE Titulo = 'Lucas'"""
    cursor.execute(sql)
    conn.commit()

def listar():
    sql = """SELECT rowid, * FROM ALBUMS ORDER BY Titulo"""
    cursor.execute(sql)
    for row in cursor.fetchall(): #seleciona todas as linhas da tabela
        print(row) #Imprime tudo