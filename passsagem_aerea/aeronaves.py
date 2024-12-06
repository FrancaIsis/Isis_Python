import sqlite3

conn = sqlite3.connect("C:/Isis_Python/Isis_Python-1/passsagem_aerea/projetos_sqlite3/BD/aeroporto.db") 

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