import sqlite3
from conexao import conectar

conn = conectar() 

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS voos (
        voo_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        data TEXT NOT NULL,
        horario TEXT NOT NULL,
        aeronave_id INTEGER,
        trecho_id INTEGER,
        foreign key (aeronave_id) references aeronaves (aeronave_id),
        foreign key (trecho_id) references trechos (trecho_id)
    )
''')

conn.commit()
conn.close()