import sqlite3

conn = sqlite3.connect("C:/Isis_Python/Isis_Python-1/passsagem_aerea/projetos_sqlite3/BD/aeroporto.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        cpf TEXT NOT NULL PRIMARY KEY,
        nome_cliente TEXT NOT NULL,
        data_nascimento TEXT NOT NULL
    )
''')