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