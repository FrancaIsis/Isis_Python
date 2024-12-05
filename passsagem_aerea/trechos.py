import sqlite3

conn = sqlite3.connect("C:/Isis_Python/Isis_Python/projetos_sqlite3/BD/aeroporto.db")

cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")
cursor.execute('''
    CREATE TABLE IF NOT EXISTS trechos (
        trecho_id INTEGER NOT NULL PRIMARY KEY,
        distancia INTEGER,
        duracao TEXT,
        aeroporto_origem INTEGER,
        foreign key (aeroporto_origem) references aeroportos (aeroporto_id),
        aeroporto_destino INTEGER,
        foreign key (aeroporto_destino) references aeroportos (aeroporto_id)
    )
    
''')

