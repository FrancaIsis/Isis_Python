import sqlite3

def conectar():
    # função para conectar com o banco de dados
    #conn = sqlite3.connect("C:/Isis_Python/Isis_Python/projetos_sqlite3/passsagem_aerea/Isis_Python/passsagem_aerea/projetos_sqlite3/BD/aeroporto.db")
    conn = sqlite3.connect("C:/Isis_Python/Isis_Python/passsagem_aerea/BD/aeroporto.db")

   
    return conn