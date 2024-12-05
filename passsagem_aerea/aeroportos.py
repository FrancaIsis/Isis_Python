import sqlite3

conn = sqlite3.connect("C:/Isis_Python/Isis_Python/projetos_sqlite3/BD/aeroporto.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS aeroportos (
        aeroporto_id INTEGER NOT NULL PRIMARY KEY,
        nome_aeroporto TEXT NOT NULL,
        cidade_id integer,
        foreign key (cidade_id) references cidades (cidade_id)
    )
''')