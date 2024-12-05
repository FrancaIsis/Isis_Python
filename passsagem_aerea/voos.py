import sqlite3

conn = sqlite3.connect("C:/Isis_Python/Isis_Python/projetos_sqlite3/BD/aeroporto.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS voos (
        voo_id INTEGER NOT NULL PRIMARY KEY,
        data TEXT NOT NULL,
        horario TEXT NOT NULL,
        aeronave_id INTEGER,
        foreign key (aeronave_id) references aeronaves (aeronave_id)
    )
''')