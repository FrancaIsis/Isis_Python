import sqlite3

def conectar():
    # função para conectar com o banco de dados
    conn = sqlite3.connect("C:/Isis_Python/Isis_Python-1/passsagem_aerea/projetos_sqlite3/BD/aeroporto.db")
    return conn