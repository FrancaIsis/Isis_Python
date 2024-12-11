import sqlite3
from conexao import conectar

conn = conectar() 

cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")
cursor.execute('''
    CREATE TABLE IF NOT EXISTS trechos (
        trecho_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        distancia INTEGER,
        duracao TEXT,
        preco REAL,
        aeroporto_origem INTEGER,
        aeroporto_destino INTEGER,
        foreign key (aeroporto_origem) references aeroportos (aeroporto_id),        
        foreign key (aeroporto_destino) references aeroportos (aeroporto_id)
    )
    
''')
conn.commit()
conn.close()

