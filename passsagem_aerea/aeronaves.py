import sqlite3
from conexao import conectar

conn = conectar() 

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS aeronaves (
        aeronave_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome_aeronave TEXT NOT NULL,
        num_poltronas INTEGER
        )
''')

conn.commit()
conn.close()