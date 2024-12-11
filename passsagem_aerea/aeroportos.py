import sqlite3
from conexao import conectar

conn = conectar() 

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS aeroportos (
        aeroporto_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome_aeroporto TEXT NOT NULL,
        cidade_id integer,
        foreign key (cidade_id) references cidades (cidade_id)
    ) 
''')

conn.commit()
conn.close()
