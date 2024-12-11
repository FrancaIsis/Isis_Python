import sqlite3
from conexao import conectar

conn = conectar() 

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cidades (
        cidade_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome_cidade TEXT NOT NULL,
        estado TEXT NOT NULL
        )  
''')

conn.commit()
conn.close()
