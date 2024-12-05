import sqlite3

conn = sqlite3.connect("C:/Isis_Python/Isis_Python/projetos_sqlite3/BD/aeroporto.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cidades (
        cidade_id INTEGER NOT NULL PRIMARY KEY,
        nome_cidade TEXT NOT NULL
        )
    
''')